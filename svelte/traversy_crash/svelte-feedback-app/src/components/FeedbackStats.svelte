<script>
	import {FeedbackStore} from "../stores";
	
	export let count
	export let avarage
	
	$: count = $FeedbackStore.length
	$: avarage = $FeedbackStore.reduce((a, {rating}) => a + rating, 0) / $FeedbackStore.length
</script>

<div class="feedback-stats">
	<h4>{count} Reviews</h4>
	<h4>Ratings Avarage: {avarage}</h4>
</div>

<style>
	.feedback-stats {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
</style>