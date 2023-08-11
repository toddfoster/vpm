# vpm
Vim Python Menus

**FALSE ALERT**? *I went to add a hotkey to my vimrc to activate this. I discovered I had already installed [vim-quickui](https://github.com/skywind3000/vim-quickui/). It's pure vimscript but could still call out to my python scripts. And the UI is already more than adequate for my needs. It may not (or may!) have the infinite nesting possibilities of a hydra. But I think it will be more than sufficient for me.* 

I want the functionality of hydras from emacs. In vim. Written in python.

These are menus I define, activated by a key (or a series of keys to traverse a
menu structure). 

I've been using emacs for a few years now. My set-up is not bad, and not
overly-complicated. But it is so painfully fragile that I keep wishing for a
change. vim always seemed bullet-proof by comparison. org-mode is the killer
feature for me in emacs: I'm not sure yet how or whether vim will compete. But
the other feature I really like is hydras.

Given a hydra with a simple leader, I can make the editor do awesome things just
for me. Like uploading an audio file to a filestore and then linking to it from
a new post on a wordpress site with an rss feed. I've not found the motivation
to learn elisp well. I certainly don't care to learn vimscript. If the world ran
on ruby, that would be kind of sweet. But python is ubiquitous and almost
brutally simple. Exactly what is needed for a once-a-year amateur coder like myself.

Vim can call python, and python can reach back into vim. I should be able to do
anything I want, as long as what I want has a simple UI. The UI is always the
hard part. That is what the initial commit is about.

This is a toy / proof-of-concept. Maybe someday it'll do something interesting.
On the other hand, today I figured out the (to me) hardest problems. Given that
I have too many hobbies, this may be as far as I get!

TODO
-----
- Find a slightly elegant way to implement nested menus.

