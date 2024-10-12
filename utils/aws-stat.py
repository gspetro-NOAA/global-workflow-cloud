import getopt
import os, sys
import types
import time
import datetime
import subprocess

import numpy as np

def cmdout(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    ostr = result.stdout
    return ostr.strip()

#------------------------------------------------------------------
""" StatsFileHandler """
class StatsFileHandler:
  """ Constructor """
  def __init__(self, debug=0, workdir=None, filename='stat.log', fcstnode=1):
    """ Initialize class attributes """
    self.debug = debug
    self.workdir = workdir
    self.filename = filename
    self.fcstnode = fcstnode

    if(workdir is None):
      print('workdir not defined. Exit.')
      sys.exit(-1)

    fullname = '%s/%s' %(workdir, filename)
    if(os.path.exists(fullname)):
      print('Filename: %s' %(fullname))
      self.fullname = fullname
    else:
      print('filenmae %s does not exist. Exit.' %(fullname))
      sys.exit(-1)

  def process(self):
    self.stats = {}
    with open(self.fullname) as fh:
      lines = fh.readlines()
      num_lines = len(lines)

      headline = lines[0].strip()

      headline = headline.replace('EXIT STATUS', 'EXIT_STATUS')
      itemlist = headline.split()

     #print('headline: ', headline)
     #print('itemlist: ', itemlist)
     #item:  ['CYCLE', 'TASK', 'JOBID', 'STATE', 'EXIT_STATUS', 'TRIES', 'DURATION']

      nl = 2
      while(nl < num_lines):
        line = lines[nl].strip()
        nl += 1
       #print('Line %d: %s' %(nl, line))
        cycle, task, jobid, state, status, tries, duration = line.split()
       #print('cycle, task, jobid, state, status, tries, duration =', cycle, task, jobid, state, status, tries, duration)

        if state in ['QUEUED', 'RUNNING']:
          cycle

        if(jobid != '-'):
          item = line.split()
         #print('Line %d: %s' %(nl, line))
         #print('cycle, task, jobid, state, status, tries, duration =', cycle, task, jobid, state, status, tries, duration)

         #nm = task.find('_mem')
          nm = task.find('_mem')
          if(nm < 0):
            nm = task.find('_ensstat_')
            if(nm > 0):
              nm = task.find('_f')
          if(nm > 0):
            subtask = task[:nm]
            if(subtask in self.stats.keys()):
             #print('cycle, task, jobid, state, status, tries, duration =', cycle, task, jobid, state, status, tries, duration)
              if(state == 'SUCCEEDED'):
                self.stats[subtask]['ns'] += 1
                self.stats[subtask]['succeed'] += float(duration)
              elif(state == 'DEAD'):
                self.stats[subtask]['nd'] += 1
                self.stats[subtask]['dead'] += float(duration)
            else:
             #print('cycle, task, jobid, state, status, tries, duration =', cycle, task, jobid, state, status, tries, duration)
              self.stats[subtask] = {}
              self.stats[subtask]['ns'] = 0
              self.stats[subtask]['nd'] = 0
              self.stats[subtask]['succeed'] = 0.0
              self.stats[subtask]['dead'] = 0.0
              if(state == 'SUCCEEDED'):
                self.stats[subtask]['ns'] = 1
                self.stats[subtask]['succeed'] = float(duration)
              else:
                self.stats[subtask]['nd'] = 1
                self.stats[subtask]['dead'] = float(duration)
          else:
            subtask = task
            self.stats[subtask] = {}
            self.stats[subtask]['ns'] = 1
            self.stats[subtask]['succeed'] = float(duration)
            self.stats[subtask]['nd'] = 0
            self.stats[subtask]['dead'] = 0.0

    print('Stats:')
    for task in self.stats.keys():
     #print('task: ', task)
     #print('self.stats[task]: ', self.stats[task])
      if(self.stats[task]['ns']):
        avg = self.stats[task]['succeed']/self.stats[task]['ns']
        print('task: %20s, number: %3d: succeed: %f, avg: %f' %(task,
          self.stats[task]['ns'],
          self.stats[task]['succeed'], avg))
      else:
        print('task: %20s, number: %3d: dead: %f' %(task,
          self.stats[task]['nd'],
          self.stats[task]['dead']))

#--------------------------------------------------------------------------------
if __name__== '__main__':
  debug = 1
  output = 0
  workdir = '/lustre/Wei.Huang/run/EXPDIR/c384sfs'
  filename = 'stat.log'
  fcstnode = 38

  opts, args = getopt.getopt(sys.argv[1:], '', ['debug=', 'workdir=',
                                                'filename=', 'fcstnode='])

  for o, a in opts:
    if o in ('--debug'):
      debug = int(a)
    elif o in ('--workdir'):
      workdir = a
    elif o in ('--filename'):
      filename = a
    elif o in ('--fcstnode'):
      fcstnode = int(a)
    else:
      assert False, 'unhandled option'

  sfh = StatsFileHandler(debug=debug, workdir=workdir,
                         filename=filename, fcstnode=fcstnode)
  sfh.process()

