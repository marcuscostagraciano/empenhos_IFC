<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart, PieChart } from 'echarts/charts'
import { DatasetComponent, GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { useAppStore } from '../stores/app'
import { onMounted, reactive } from 'vue'
import app from '@/services/app'

const appStore = useAppStore()

onMounted(async () => {
  await appStore.getCharts()
})

use([
  CanvasRenderer,
  LineChart,
  PieChart,
  LegendComponent,
  TooltipComponent,
  DatasetComponent,
  GridComponent,
])

provide(THEME_KEY, 'default')
</script>

<template>
  <div class="chart-dataset ma-16">
    <TitleSection title="Total de Recursos Empenhados e Liquidados" />
    <v-chart class="chart" :option="appStore.mainChart"/>
  </div>
</template>

<style lang="css" scoped>
  .chart-dataset {
    height: 400px;
  }
</style>
