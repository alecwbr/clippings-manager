<script setup>
import axios from "axios"
import { reactive, onMounted } from "vue"
import AuthorList from "./components/AuthorList.vue"
import BookClips from "./components/BookClips.vue"

const state = reactive({
  authors: [],
  activeBook: { author: null, book: { id: null, name: null, author_id: null, clips: null } }
});

async function getAuthors() {
  let res = await axios.get("/api/authors")
  state.authors = res.data
}

async function setActiveBook(book) {
  state.activeBook = book
}

async function deleteClip(id) {
  let res = await axios.delete(`/api/clips/${id}`)
  state.activeBook.book.clips = state.activeBook.book.clips.filter(clip => clip.id !== id)
}
onMounted(async () => {
  await getAuthors()
});
</script>

<template>
  <main class="main">
    <div class="side-bar">
      <AuthorList
        :authors="state.authors"
        @select-book="setActiveBook"
      ></AuthorList>
    </div>
    <div class="clips">
      <BookClips :active-book="state.activeBook"
            @delete-clip="deleteClip">
      </BookClips>
    </div>
  </main>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
}

@media screen and (min-width: 600px) {
  .main {
    flex-direction: row;
  }

  .clips {
    flex: 1;
  }

  .side-bar {
    width: 300px;
    position: sticky;
    top: 0;
  }
}
</style>
