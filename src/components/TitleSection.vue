<script setup>
defineProps(['title', 'subtitle'])
</script>

<template>
    <h4 class="text-subtitle-1 text-grey pb-4">{{ title }}</h4>
    <p class="text-grey" v-if="subtitle">{{ subtitle }}</p>
</template>