# 0x06. Star Wars API

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

<p>Write a script that prints all characters of a Star Wars movie:</p>
<ul>
<li>The first positional argument passed is the Movie ID - example: <code>3</code> = “Return of the Jedi” </li>
<li>Display one character name per line <strong>in the same order as the “characters” list in the <code>/films/</code> endpoint</strong></li>
<li>You must use the <a href="/rltoken/gh_NaSUk9QlXHVoACFU-tg" title="Star wars API" target="_blank">Star wars API</a></li>
<li>You must use the <code>request</code> module</li>
</ul>
<pre><code>alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
</code></pre>