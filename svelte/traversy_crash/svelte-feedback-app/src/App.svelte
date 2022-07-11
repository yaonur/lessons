<script>
	import FeedbackList from './components/FeedbackList.svelte'
	import FeedbackStats from "./components/FeedbackStats.svelte";
	import FeedbackForm from "./components/FeedbackForm.svelte";
	
	let feedback = [
		{
			id: 1,
			rating: 11,
			text: 'one'
		},
		{
			id: 2,
			rating: 21,
			text: 'two'
		}
		, {
			id: 3,
			rating: 31,
			text: 'three'
		}
	
	]
	
	$: count = feedback.length
	$: avarage = feedback.reduce((a, {rating}) => a + rating, 0) / feedback.length
	
	const deleteFeedback = (e) => {
		const itemId = e.detail
		feedback = feedback.filter((item) => item.id != itemId)
	}
</script>

<main class="container">
	<FeedbackForm/>
	<FeedbackStats {count} {avarage}/>
	<FeedbackList {feedback} on:delete-feedback={deleteFeedback}/>
</main>
