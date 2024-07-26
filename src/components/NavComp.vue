<script setup>
import { useAppStore } from "../stores/app";

const appStore = useAppStore();
</script>

<template>
  <nav class="w-100 pb-8 d-flex justify-space-between align-end">
    <v-btn
      :color="appStore.themeColor === 'light' ? 'dark' : 'light'"
      prepend-icon="mdi-keyboard-backspace"
      variant="plain"
    >
      Voltar ao Portal IFC
    </v-btn>
    <div>
      <v-btn
        v-if="appStore.themeColor === 'light'"
        color="light"
        icon="mdi-white-balance-sunny"
        variant="plain"
        @click.stop="appStore.setTheme('dark')"
      ></v-btn>
      <v-btn
        v-else
        color="dark"
        icon="mdi-moon-waning-crescent"
        variant="plain"
        @click.stop="appStore.setTheme('light')"
      ></v-btn>
      <v-btn
        :color="appStore.themeColor === 'light' ? 'dark' : 'light'"
        icon="mdi-information-slab-circle-outline"
        variant="plain"
      ></v-btn>
    </div>
  </nav>
</template>
