# -*- coding: utf-8 -*-
"""
    backup_full
    ~~~~~~~~~~~~
    This script's purpose is to make backup full from a root directory
"""

import subprocess
import time
import sys

def log_start(hourIni):
    """Responsible for generates a banner with the start time of the Backup"""

    start = '''
  ===========================================================================
||                                                                           ||
||          ___    ______              ______        __          __          ||
||         /   |  / / __/_______  ____/ / __ \____  / /_  ____  / /_         ||
||        / /| | / / /_/ ___/ _ \/ __  / /_/ / __ \/ __ \/ __ \/ __/         ||
||       / ___ |/ / __/ /  /  __/ /_/ / _, _/ /_/ / /_/ / /_/ / /_           ||
||      /_/  |_/_/_/ /_/   \___/\__,_/_/ |_|\____/_.___/\____/\__/           ||
||                                                                           ||
||                       BACKUP FULL OF FILESERVER                           ||
||                                                                           ||
  ===========================================================================
  ===========================================================================
                 BACKUP FULL OF FILESERVER BEGINNER TO %s
  ===========================================================================
''' % hourIni
    return start

def log_end(dateIni, hourIni, backup, pathlog):
    """Responsible for making the calculations and generate the log end"""
    today   = (time.strftime("%d-%m-%Y"))
    hourEnd = time.strftime('%H:%M:%S')
    backup  = backup.replace('tar cvfP', '')
    final   = '''
  ===========================================================================
                            BACKUP FULL FINISHED
                START TIME:     %s  -  %s
                END TIME  :     %s  -  %s
                LOG FILE  :     %s
                BAK FILE  :     %s
  ===========================================================================
    ''' % (dateIni, hourIni, today, hourEnd, pathlog, backup)
    return final

def dismount_hd(disk):
    """Responsible for dismount HD for safety
    By default this function has commented in the main function"""
    try:
        umount = 'umount %s' % disk
        subprocess.call(umount, shell=True)
        return True
    except:
        return False

def mount_log(file):
    """Responsible for creating the log file"""
    date = (time.strftime("%Y-%m-%d"))
    logfile     = '%s_backup_full.txt' % date
    # pathlog     = '/home/neldev/workspace/python_backup/log/%s' % logfile
    pathlog     = '{}{}'.format(file, logfile)

    return pathlog

def mount_backup(origin, dest):
    """Responsible for assembling the backup command"""
    date = (time.strftime("%Y-%m-%d"))
    backupfile = '%s-backup_full.tar.gz' % date
    pathdest   = '{}{}'.format(dest, backupfile)
    pathorigin = '{}'.format(origin)
    backup     = 'tar cvfP %s %s' % (pathdest, pathorigin)

    return backup

def backupfull():
    """Responsible for running the backup full

        Args are the absolute paths
        ---------------------------------------
        First:  path destination (backup directory)
        Second: path origin (where it will be saved)
        Third:  path log
    """

    #Defines where the partition that will be used to store the backup
    # disk     = '/dev/sdb'
    hourIni = time.strftime('%H:%M:%S')
    backup   = mount_backup(sys.argv[1], sys.argv[2])
    pathlog  = mount_log(sys.argv[3])
    start    = log_start(hourIni)

    #Printa o Banner
    l = open(pathlog, 'w')
    l.write(start)
    l.close()

    #Mounts all disks that are in FSTAB
    mount = 'mount -a'
    subprocess.call(mount, shell=True)

    #Run the backup
    subprocess.call(backup, shell=True)

    #Print the final log
    dateIni = (time.strftime("%d-%m-%Y"))
    final   = log_end(dateIni, hourIni, backup, pathlog)
    r       = open(pathlog, 'a')
    r.write(final)
    r.close()

    #Uncomment this function to remove the partition that will be used to store the backup
    #dismount_hd(disk)


if __name__ == '__main__':
    backupfull()