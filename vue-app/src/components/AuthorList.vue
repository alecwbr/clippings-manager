<script setup>
import { ref } from 'vue'

const activeIndex = ref(0)

const props = defineProps({
    authors: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['selectBook'])

function handleAuthorClick(index) {
    activeIndex.value = index
}

function handleBookClick(author_book, index) {
    activeIndex.value = index
    emit('selectBook', author_book)
}
</script>

<template>
    <div v-for="(author, aIndex) in props.authors"
        :key="author.id"
        class="author"
        :class="{ 'active': activeIndex === aIndex }"
        @click="handleAuthorClick(aIndex)">
        {{ author.name }}
        <div v-if="activeIndex === aIndex">
            <ul>
                <li v-for="(book, bIndex) in author.books"
                    :key="book.id"
                    @click="handleBookClick({ author: author.name, book }, bIndex)">
                    {{ book.name }}
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.active {
    color: red;
}

.author {
    cursor: pointer;
}
</style>