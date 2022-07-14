<script>
	import {createEventDispatcher} from 'svelte';
	
	let dispatch = createEventDispatcher();
	
	let name;
	let beltColour;
	let age;
	// let fighting
	// let sneaking;
	// let running;
	let skills = [];
	const handleSubmit = () => {
		const person = {
			name,
			beltColour,
			age,
			skills,
			id: Math.random()
		}
		dispatch('addPerson', person);
	}
</script>


<form on:submit|preventDefault={handleSubmit}>
	<h3>Add Person</h3>
	<input type="text" placeholder="name" bind:value={name}>
	<input type="number" placeholder="age" bind:value={age}>
	<label>Skills</label>
	<input type="checkbox" bind:group={skills} value="fighting">fighting<br>
	<input type="checkbox" bind:group={skills} value="sneaking">sneaking<br>
	<input type="checkbox" bind:group={skills} value="running">running<br>
	<label>Belt Color</label>
	<select name="" id="" bind:value={beltColour}>
		<option value="black">black</option>
		<option value="orange">orange</option>
		<option value="brown">brown</option>
		<option value="white">white</option>
	</select>
	                                                            <!--	<input type="checkbox" bind:checked={fighting}>fighting<br>-->
	                                                            <!--	<input type="checkbox" bind:checked={sneaking}>sneaking<br>-->
	                                                            <!--	<input type="checkbox" bind:checked={running}>running<br>-->
	<button>Add Person</button>
</form>
<!--	<div slot="title">-->
<!--		<h3>Add a New Person</h3>-->
<!--	</div>-->
<style>

</style>
