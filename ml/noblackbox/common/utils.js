const utils={}
utils.printProgress=(count,max)=>{
	process.stdout.clearLine();
	process.stdout.cursorTo(0);
	process.stdout.write(`Processing ${count}/${max}`);
}

utils.groupBy=(objArray,key)=> {
	const groups={}
	for(let obj of objArray){
		const value=obj[key]
		console.log(obj)
		if(groups[value]==null){
			groups[value]=[]
		}
		groups[value].push(obj)
	}
	return groups
}

if(typeof module!=='undefined'){
	module.exports=utils
}

