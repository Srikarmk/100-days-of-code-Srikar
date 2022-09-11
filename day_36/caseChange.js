var myName=prompt("Name:");

firstLetter=myName.slice(0,1);
firstLetter=firstLetter.toUpperCase();
restOfName=myName.slice(1,myName.length);
restOfName=restOfName.toLowerCase();
fullString="Hello "+firstLetter+restOfName;
alert(fullString)