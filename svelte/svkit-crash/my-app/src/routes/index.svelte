<script>
	import {pokemon} from "../stores/pokestore.js"
	import PokemanCard from "../components/pokemanCard.svelte"
	
	let searchTerm = "";
	let filteredPokemon = [];
	$: {
		console.log(searchTerm)
		if (searchTerm) {
			filteredPokemon = $pokemon.filter(pokeman => pokeman.name.includes(searchTerm))

		} else {
			filteredPokemon = [...$pokemon]
		}
	}
	
</script>

<svelte:head>
	<title>About svelte pokedex</title>
</svelte:head>

<h1 class="text-3xl text-center my-8 uppercase">Svelte Kit Pokedex</h1>
<input type="text" placeholder="Search Pokemon" class="w-full rounded-md text-lg p-3 border-2 border-gray-200"
       bind:value={searchTerm}>
<div class="py-4 grid gap-4 md:grid-cols-2 grid-cols-1">
	{#each filteredPokemon as pokeman}
		<PokemanCard pokeman={pokeman}></PokemanCard>
	{/each}
</div>
<style>

</style>
