<script setup>
const props = defineProps({
    activeBook: {
        type: Object,
        required: true
    }
})

const emit = defineEmits(['deleteClip'])

function formatDate(date) {
    let d = new Date(date)
    return `${d.toLocaleDateString()} at ${d.toTimeString()}`
}

function handleDeleteClipButton(clipId) {
    emit("deleteClip", clipId)
}

function formatAuthor(author) {
    if (author.includes(',')) {
        let splitName = author.split(',')
        return `${splitName[1]} ${splitName[0]}`
    }
    return author
}
</script>

<template>
    <div v-if="props.activeBook.book !== null" class="wrapper">
        <h2>{{ props.activeBook.book.name }}</h2>
        <div class="clip-wrapper" v-for="clip in props.activeBook.book.clips" :key="clip.id">
            <div><span>location: {{ clip.location }}</span></div>
            <div><span>date: {{ formatDate(clip.date) }}</span></div>
            <div><span>type: {{ clip.clip_type }}</span></div>
            <br />
            <div>&quot;{{ clip.highlight }}&quot;</div>
            <div>- {{ formatAuthor(props.activeBook.author) }}</div>
            <button>tag</button>
            <button @click="handleDeleteClipButton(clip.id)">delete</button>
        </div>
    </div>
</template>

<style scoped>
h2 {
    text-align: center;
}

.clip-wrapper {
    border: 1px solid black;
    padding: 10px;
    margin-bottom: 10px;
}
</style>