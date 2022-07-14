<script>
	import Modal from './Modal.svelte'
	import AddPersonForm from "./AddPersonForm.svelte";
	
	let showModal = false;
	const toggleModal = () => {
		showModal = !showModal
	}
	let people = [
		{name: 'yoshi', beltColour: 'black', age: 25, id: 1},
		{name: 'mario', beltColour: 'orange', age: 25, id: 2},
		{name: 'luigi', beltColour: 'brown', age: 25, id: 3},
	]
	const handleClick = (id) => {
		people = people.filter((person) => {
			return person.id != id
		})
	}
	const addPerson = (e) => {
		// console.log(e.detail)
		const person = e.detail;
		people = [person, ...people]
	}
	let num = 5;

</script>
<Modal message="im a prop" isPromo={false} {showModal} on:click={toggleModal}>
	<AddPersonForm on:addPerson={addPerson}/>
</Modal>

<main>
	{#each people as person (person.id)}
		<div>
			<button on:click|once={toggleModal}>Open Modal</button>
			<h4>{person.name}</h4>
			{#if person.beltColour === 'black'}
				<p></p><strong>master ninjakkkk</strong>
			{/if}
			<p>{person.age} years old, {person.beltColour} belt.</p>
			<div>
				{#if person.skills}
					{#each person.skills as skill }
						<p>{skill}</p>
					{/each}
				{/if}
			</div>
			<button on:click={()=>handleClick(person.id)}>Delete</button>
		</div>
	{:else}
		<p>There are no people to show...</p>
	{/each}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>