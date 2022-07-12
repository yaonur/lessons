import {writable} from 'svelte/store'

export const FeedbackStore = writable([
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
])