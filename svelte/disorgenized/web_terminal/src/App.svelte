<script lang="ts">
	import TerminalInput from "./components/TerminalInput.svelte"
</script>

<main id="root">
	<section class="center" id="window"></section>
	<section class="center" id="terminal">
		<TerminalInput></TerminalInput>
	
	</section>
</main>

<style>
	#root {
		height: 100vh;
		width: 100vw;
		background: rgb(2, 0, 36);
		background: linear-gradient(90deg, rgba(2, 0, 36, 1) 0%, rgba(98, 2, 152, 1) 0%, rgba(0, 212, 255, 1) 100%);
		
		display: grid;
		grid-template-columns:repeat(12, 1fr);
		grid-template-rows:repeat(12, 1fr);
	}
	
	.center {
		grid-column-start: 4;
		grid-column-end: 10;
		grid-row-start: 4;
		grid-row-end: 10;
	}
	
	#window {
		
		background-color: black;
		opacity: .5;
		border-radius: 10px;
	}
	
	#terminal {
		background-color: transparent;
		padding: 1em;
		z-index: 10;
		
	}
</style>
