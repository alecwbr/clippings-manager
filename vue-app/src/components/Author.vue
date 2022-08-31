<script setup>

const props = defineProps({
    author: {
        type: Object,
        required: true
    }
})

const emit = defineEmits(['selectAuthor'])

function selectAuthorClick() {
    emit('selectAuthor', props.author.id)
}
</script>

<template>
    <div class="author" @click="selectAuthorClick">{{ author.name }}</div>
</template>