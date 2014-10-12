# Copyright (c) 2014, Ruslan Baratov
# All rights reserved.

import detail.call

def run(config, verbose, cpack_generator):
  pack_command = ['cpack']
  if config:
    pack_command.append('-C')
    pack_command.append(config)
  if verbose:
    pack_command.append('--verbose')
  if cpack_generator:
    pack_command.append('-G{}'.format(cpack_generator))
  detail.call.call(pack_command, verbose)
