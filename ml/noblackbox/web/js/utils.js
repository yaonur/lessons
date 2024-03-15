const utils={}
utils.printProgress=(count,max)=>{
	process.stdout.clearLine();
	process.stdout.cursorTo(0);
	process.stdout.write(`Processing ${count}/${max}`);
}


