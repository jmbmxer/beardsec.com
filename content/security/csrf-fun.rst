=======================
Encounters with CSRF
=======================
:date: 2014-02-21
:tags: CSRF,  Attacks,  OWASP,  Penetration Testing

Introduction
================

Cross-site request forgery, mostly commonly known as CSRF is by far one of my favorite web application attacks. Over the past several years I have been lucky enough to get written permission to perform vulnerability assessments on a large amount of really interesting web applications.  CSRF is something preach about to my clients, and one of my most commonly discovered vulnerabilities.

CSRF works best as a targeted attack or as a result of a stored injection attack.  It relies on a victim being logged into a vulnerable web application and them clicking on a specially crafted link.

Links for Everyone!
=====================

Let's say that a user is logged into their favorite social networking website where links being flung around wildly and the user base is less than tech savvy. This pretend social networking site also decided to not require the user to enter their current password when they want to create a new one. Since anyone can join this site, post content, and add people as their "friends", the resident basement script kiddie sets up a fake account and pokes around. He finds a co-worker that has been giving him a really hard time and evil thoughts cross his mind.  The bad guy knows how easy CSRF vulnerabilities are to discover so he starts with the keys to the kingdom, the password reset page.  He notices that the only fields being passed in the POST request are the new password and a confirmation of the new password so he crafts up this basic HTML page and throws it up on his server.

.. code-block:: html

	<html>
  	  <body>
   	     <form action="https://socialbutterfly.com/Users/JerkCoWorker/password_reset" method="POST">
   	      <input type="hidden" name="newpass" value="G0tcha!" />
     	      <input type="hidden" name="newpass_confirm" value="G0tcha!" />
     	      <input type="image" src="clickme.png" value="Submit request" />
    	      </form>
 	 </body>
	</html>


He then posts a link to his co-workers wall or sends him a private message with the following deceptively sly image.

.. image:: http://beardsec.com/images/clickhere.jpg
  :height: 292px
  :width: 340px
  :align: center

This image is not what it seems. When clicked, it executes the HTML POST request on behalf of the victim. Since there is no CSRF token or any value only known to the user (such as the current password), the victims password is changed to G0tcha! and the basement hacker wins, he is able to log into his co-workers account and wreak havoc on his co-workers social life.

Mitigations
================

This is a pretty simple example, CSRF can get quite complex. While the majority of your sensitive actions in a web application are performed over a POST request, I have encountered GET requests that download files or perform other actions. Take the following URL for example.

.. code-block:: html

	GET https://topsecretfilesharingapp.com/download/filemightbemalicious.exe

Since downloads are being handled via a GET request and the application might not be handling malicious file uploads in a secure manner, we can force a user to download an executable or Java file just by having them click on a link.

There are a few ways to actually combat the CSRF attack, all of them require a special, private piece of information that only the user knows or can prove that the request is actually coming from that page with the valid user iniating that action.  Below is a list of mitigations ranked from most logical and invisible to the end user to the worst possible UX ever and should be avoided at all costs.

1. CSRF Tokens in HTTP Requests - This is the most common mitigation to CSRF attacks and thankfully is becoming easier to implement in popular frameworks such as Django and Ruby on Rails.  This works by having a hidden field in requests that is tied to the users current session. It is also possible to implement a new, random CSRF token per request but issues may arise with using the back button while logged in to the application.  With a CSRF token in place, even if a malicious user were to send an unsuspecting person a link the transaction would not go through because the server denies any request lacking a CSRF token or with the incorrect CSRF token value.:

.. code-block:: html

	<form action="/changepassword.php" method="post">
 		 <input type="hidden" name="CSRFToken" value="OWY4NmQwODE4ODRjN2A90WEwYzU1YWQwMTVhM2JmNGYxYjJiMGI4MjJjZDE1ZDZjMTVi
 	 MGYwMGEwOA==">
 	 </form>


It should be mentioned that passing this value in the URL does in fact work to protect against CSRF attacks. But as a security guy I cringe when I see any token in the URL. Keep sensitive data away from the URL. What if someone copy and pastes a link to a co-worker or an internal WAF/ Reverse Proxy can grab the token?  It's better to keep it away from prying eyes.

2. Header checking - Having the server check for an HTTP referrer header or origin header can be an effective way to mitigate CSRF attacks and has been used for quite some time in embedded devices that do not necessarily rely on sessions.  These methods are helpful but do present challenges such as redirect vulnerabilities and URL spoofing.  Use header checking sparingly, only if CSRF tokens are an impossible feat.

3. Challenge - Response- If you want to scare your users away from your shiny new web application make them answer a Captcha on every sensitive request.  While making users enter their password or a unique Captcha per request can mitigate CSRF attacks, why do it?  There are better options than this. That is all.

There you have it, my thoughts on CSRF and why it is awesome.  Go fire up an intercepting proxy and build some proof of concept HTML pages and hack away. Legally, of course.
