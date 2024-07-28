<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart, PieChart } from 'echarts/charts'
import { DatasetComponent, GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { useAppStore } from '../stores/app'
import { onMounted } from 'vue'

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

// const onEvents = {
//   updateAxisPointer: event => {
//     const xAxisInfo = event.axesInfo[0]
//     if (xAxisInfo) {
//       const dimension = xAxisInfo.value + 1
//       option.series.forEach(serie => {
//         if (serie.id === 'pie') {
//           serie.label.formatter = `{b}: {@[${dimension}]} ({d}%)`
//           serie.encode.value = dimension
//           serie.encode.tooltip = dimension
//         }
//       })
//     }
//   },
// }
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
