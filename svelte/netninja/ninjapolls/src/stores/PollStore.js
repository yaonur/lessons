import { writable } from "svelte/store"

const PollStore = writable([
    {
        id: 1,
        question: "Python or JavaScript?",
        answerA: "Python",
        answerB: "JavaScript",
        votesA: 9,
        votesB: 5,
    },
])

export default PollStore
