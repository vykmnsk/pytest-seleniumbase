Bugs Found
==========


Manually
--------

All browsers

* (Prod) no articles in a category - empty link 
* chat error status "Try again later" after closing
* Y/N feedback: is not restricted to 280 chars.  
* Y/N feedback: placeholder overlaps when text doesn’t fit in the box
* Y/N feedback: linebreak auto-removed when typing
* URL redirect - empty page instead of level up
* responsive screen: breakpoints show/hide elements
* responsive screen: empty/less data  
* very long article name stretches the links section beyond 2/3
* more than 2 lines for question header -> overlapping summary
* accordion opens off-screen when at the bottom
* single accordion shows collapsed
* text “7 am-7 pm ” breaks to the next line
* double spaces in text copy
* 5 microsite links pointing to the old H&S
* distorted pre-existing Contact Us on screen re-size
* placement tiles merge and diff sizes

IE11

* CMS chat not connecting at Home page
* Call action Login box distorted
* "x" in Search Input bar
* '>' shevron not animated



with Automation
----------------

When developing

* wrong page Title
* missing page Header
* tile images missing data-ids
* nested anchor tags
* H2 is skipped
* double H2 el (hidden and visible)


When running tests

* CMS content lost labels after migration
* typos in Headers
* environment - lost CMS access
* (Prod) Trending q-s dissapeared from categories
* IE11 jumbled up in mobile size
* Large search description was not capped at 100 ch 

