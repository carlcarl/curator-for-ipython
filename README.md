小海嚴選 for IPython
====================

# Installation

Checkout the repo:

    git clone https://github.com/carlcarl/curator-for-ipython.git
    cd curator-for-ipython
    
Add your API token in `curator.py`:

    # Set your token here
    token = 'blahblah'    
    
Copy the extension to the `extensions` folder:

    cp curator.py ~/.ipython/extensions/
    
Edit IPython notebook config to enable the extension to the specific profile, here use `profile_default`:

    vim ~/.ipython/profile_default/ipython_notebook_config.py
    
Add `curator` to `c.IPKernelApp.extensions` in `ipython_notebook_config.py`:

    c.IPKernelApp.extensions = [
        'curator',
    ]

# Commands

    # 正妹隨選
	heyhey

	# 今日正妹
	heyhey today

	# 今日正妹(多圖)
	heyhey today more

# Example

![小海嚴選正妹](http://i.imgur.com/LRLEbX3.jpg)
