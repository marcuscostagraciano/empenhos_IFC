<template>
  <div class="mx-4 mt-16">
    <p class="text-caption position-fixed top-0 left-0 pa-2 text-red">
      {{ appStore.state.datas }}
    </p>
    <HeaderComp />
    <GlobalIndicators />
    <MainChart />
  </div>
</template>

<script setup>
import { useAppStore } from '@/stores/app';

const appStore = useAppStore();

onMounted(async () => {
  await appStore.getCharts();
});
</script>
