# eBay_Wesbite

In Step 1: I can able to do this step. At first, I do it Django crispy form for authentication later I notice that here no complex authentication is needed, so it is simple for me to do this step.


Step 2:After login in dashboard page, I can able to allows the user to create an auction item, for this, I added a form that takes the input input
Product Name, Product Description, Minimum Bid Price, and Auction
End DateTime.


Step 6: I tried to make everything looks pretty.


Step 7:For deploying it in Heroku, after ‘git push Heroku main’ command there arises an error. E.g;

remote:!       Push rejected to djangotask005.
remote:
To https://git.heroku.com/djangotask005.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/djangotask005.git'
G:\eBay_Wesbite\eBay>


I’m tried a lot for deploying my Django app on Heroku later unable to reach steps 3, 4, and 5. I tried to solve this from here: https://www.onooks.com/django-app-heroku-deployment-app-not-compatible-with-buildpack/
Soloution: 
Step 1) First setup the buildpack (programming-language )
Step 2) git init and currently used directory is different, so this error is still thrown “App not compatible with buildpack:”
But unfortunately it could not fixed.
