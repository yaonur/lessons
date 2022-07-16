<script>
    // import { onMount, onDestroy } from "svelte"
    import { fade, slide, scale } from "svelte/transition"
    import { flip } from "svelte/animate"
    import PollDetails from "./PollDetail.svelte"
    import PollDetail from "./PollDetail.svelte"
    import PollStore from "../stores/PollStore"

    // export let polls = []

    // const unsub = PollStore.subscribe((data) => {
    //     polls = data
    // })
    // onDestroy(() => {
    //     //unsub from store
    //     unsub()
    // })
</script>

<div class="poll-list">
    {#each $PollStore as poll}
        <div in:fade out:slide|local animate:flip={{ duration: 500 }}>
            <PollDetails {poll} />
        </div>
    {/each}
</div>

<style>
    .poll-list {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 20px;
    }
</style>
