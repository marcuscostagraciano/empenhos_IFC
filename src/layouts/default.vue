<template>
  <v-app :theme="appStore.themeColor">
    <v-main>
      <router-view />
    </v-main>
    <FooterComp />
  </v-app>
</template>

<script setup>
import { useAppStore } from '../stores/app';

const appStore = useAppStore();
</script>
