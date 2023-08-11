#!/usr/bin/python3

# python3 << python_done

# Doc's
## :help python-vim
## - vim.current.window/buffer/line/range
## Getting user input from a script in vim: https://vim.fandom.com/wiki/User_input_from_a_script

keep_running = True

import vim
def python_input(message = 'input'):
  vim.command('call inputsave()')
  vim.command("let user_input = input('" + message + ": ')")
  vim.command('call inputrestore()')
  return vim.eval('user_input')

def python_getchar(message = 'input'):
  print(message)
  vim.command("let c = getchar()")
  return vim.eval('nr2char(c)')

def demo():
  curline = vim.current.line
  name = python_input('Enter name')
  vim.current.line = curline + ' ' + name

# Prompt
def vpm_prompt():
  key = python_getchar('vpm>')
  if (key == '?'):
      vim.command("clear")
      print ("Hit 'q' to quit")
  if (key == 'q'):
      global keep_running
      keep_running = False
  if (key == 'c'):
      vim.command("redraw")
  print(f"Key pressed: {key}")

#python_done

#vim.command("set cmdheight=20")
#cmdheight = vim.eval("set cmdheight")
#print(f"cmdheight = {cmdheight}")

while keep_running:
  vpm_prompt()

#vim.command("clear")
vim.command("redraw")
#vim.command("set cmdheight=1")

