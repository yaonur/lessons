<script>
	export let pokeman;
</script>
<a href={`/pokemon/${pokeman.id}`} class="p6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md
flex flex-col items-center">
	<img class="h-40 w-40" src={pokeman.image} alt={pokeman.name}>
	<h2 class="uppercase text-2xl">{pokeman.id}. {pokeman.name}</h2>
</a>