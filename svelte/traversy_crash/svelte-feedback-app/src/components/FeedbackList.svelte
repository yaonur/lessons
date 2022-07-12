<script>
	// import {onMount, onDestroy} from 'svelte'
	import {FeedbackStore} from "../stores";
	import FeedbackItem from './FeedbackItem.svelte'
	import {fade, scale} from 'svelte/transition'
	
	// let feedback = FeedbackStore
	// const unsubscribe = FeedbackStore.subscribe((data) => feedback = data)
	// onDestroy(() => {
	// 	unsubscribe()
	// })
	

</script>
{#each $FeedbackStore as fb }
	<div in:scale out:fade>
		<FeedbackItem item={fb} />
	</div>

{/each}