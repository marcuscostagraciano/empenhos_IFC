<script lang="ts" setup>
</script>

<template>
  <div class="mx-16 mt-8">
    <h4 class="text-subtitle-1 text-grey pb-4">Indicadores Gerais</h4>
    <v-row>
      <v-col lg="4" sm="12">
        <IndicatorItem :value="4162400.11" label="Montante Empenhado" />
      </v-col>
      <v-col lg="4" sm="12">
        <IndicatorItem :value="1490515.02" label="Montante Liquidado" />
      </v-col>
      <v-col lg="4" sm="12">
        <IndicatorItem :value="-2671885.09" label="Montante Pendente de Liquidação" />
      </v-col>
    </v-row>
  </div>
</template>
