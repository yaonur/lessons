<script lang="ts">
	import {onMount} from "svelte";
	
	let terminalInput: HTMLSpanElement = null;
	onMount(() => {
		terminalInput.focus()
		d
	})
</script>

<span bind:this={terminalInput} contenteditable="true" data-path="~/Development/ "></span>
<style>
	span {
		color: lime;
		outline: none;
	}
	
	span::before {
		content: attr(data-path);
		color:coral;
	}
	
	span::after {
		content: ".";
		color:lime;
		background-color: lime;
		animation: blink infinite linear 1s;
	}
	
	@keyframes blink{
		from {opacity:1;}
		to {opacity:0;}
	}
</style>