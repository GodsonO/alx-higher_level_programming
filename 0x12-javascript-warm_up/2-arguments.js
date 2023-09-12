#!/usr/bin/node
const argument = process.argv.length;

if (argument === 3)
{
	console.log('Argument' + ' found');  
}
else if (argument > 3)
{
        console.log('Arguments found');
}
else 
{
	console.log('No argument');
}
