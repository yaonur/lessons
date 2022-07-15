<script>
    import PollStore from "../stores/PollStore.js"
    import Button from "../shared/Button.svelte"
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher()

    let fields = { question: "", answerA: "", answerB: "" }
    let errors = { question: "", answerA: "", answerB: "" }
    let valid = false
    let colors = { error: "#d91b42" }

    const submitHandler = () => {
        valid = true
        if (fields.question.trim().length < 5) {
            valid = false
            errors.question = "Question must be at least 5 characters long"
        } else {
            errors.question = ""
        }
        if (fields.answerA.trim().length < 1) {
            valid = false
            errors.answerA = "Answer A cannot be empty"
        } else {
            errors.answerA = ""
        }
        if (fields.answerB.trim().length < 1) {
            valid = false
            errors.answerB = "Answer B cannot be empty"
        } else {
            errors.answerB = ""
        }
        if (valid) {
            let poll = { ...fields, votesA: 0, votesB: 0, id: Math.random() }
            // save poll to store
            PollStore.update((currentPolls) => {
                return [poll, ...currentPolls]
            })
            dispatch("add", poll)
        }
    }
</script>

<form on:submit|preventDefault={submitHandler}>
    <div class="form-field">
        <label for="question">Poll Question</label>
        <input type="text" id="question" bind:value={fields.question} />
        <div class="errors">{errors.question}</div>
    </div>

    <div class="form-field">
        <label for="answer-a">Answer A:</label>
        <input type="text" id="answer-a" bind:value={fields.answerA} />
        <div class="errors">{errors.answerA}</div>
    </div>
    <div class="form-field">
        <label for="answer-b">Answer B:</label>
        <input type="text" id="answer-b" bind:value={fields.answerB} />
        <div class="errors">{errors.answerB}</div>
    </div>
    <Button type="primary" flat={true} inverse={true}>Add Poll</Button>
</form>

<style>
    form {
        width: 400px;
        margin: 0 auto;
        text-align: center;
    }

    .form-field {
        margin: 18px auto;
    }

    input {
        width: 100%;
        border-radius: 6px;
    }

    label {
        margin: 10px auto;
        text-align: left;
    }

    .errors {
        font-weight: bold;
        font-size: 12px;
        color: #d91b42;
    }
</style>
