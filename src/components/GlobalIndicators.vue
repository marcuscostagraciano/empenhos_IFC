<script setup>
import { useAppStore } from '@/stores/app';

const appStore = useAppStore();
</script>

<template>
  <div class="mx-16 mt-8">
    <h4 class="text-subtitle-1 text-grey pb-4">Indicadores Gerais</h4>
    <v-row>
      <v-col lg="4" sm="12">
        <IndicatorItem :value="appStore.committed" label="Montante Empenhado" />
      </v-col>
      <v-col lg="4" sm="12">
        <IndicatorItem :value="appStore.settled" label="Montante Liquidado" />
      </v-col>
      <v-col lg="4" sm="12">
        <IndicatorItem :isNegative="true" :value="appStore.balance" label="Montante Pendente de Liquidação" />
      </v-col>
    </v-row>
  </div>
</template>
