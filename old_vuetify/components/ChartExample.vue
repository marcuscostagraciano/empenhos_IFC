<script lang="ts" setup>
  import { use } from 'echarts/core'
  import { CanvasRenderer } from 'echarts/renderers'
  import { LineChart, PieChart } from 'echarts/charts'
  import { DatasetComponent, GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'
  import VChart, { THEME_KEY } from 'vue-echarts'
  import { provide, reactive, ref } from 'vue'

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

  const option = reactive({
    legend: {},
    tooltip: {
      trigger: 'axis',
      showContent: false,
    },
    dataset: {
      source: [
        ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
        ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
        ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
        ['Cheese Cocoa', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
        ['Walnut Brownie', 25.2, 37.1, 41.2, 18, 33.9, 49.1],
      ],
    },
    xAxis: { type: 'category' },
    yAxis: { gridIndex: 0 },
    grid: { top: '55%' },
    series: [
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' },
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' },
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' },
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' },
      },
      {
        type: 'pie',
        id: 'pie',
        radius: '30%',
        center: ['50%', '25%'],
        emphasis: {
          focus: 'self',
        },
        label: {
          formatter: '{b}: {@2012} ({d}%)',
        },
        encode: {
          itemName: 'product',
          value: '2012',
          tooltip: '2012',
        },
      },
    ],
  })

  const onEvents = {
    updateAxisPointer: event => {
      const xAxisInfo = event.axesInfo[0]
      if (xAxisInfo) {
        const dimension = xAxisInfo.value + 1
        option.series.forEach(serie => {
          if (serie.id === 'pie') {
            serie.label.formatter = `{b}: {@[${dimension}]} ({d}%)`
            serie.encode.value = dimension
            serie.encode.tooltip = dimension
          }
        })
      }
    },
  }
</script>

<template>
  <div class="chart-dataset ma-16 bg-grey-lighten-5 border-sm">
    <v-chart class="chart" :option="option" @events="onEvents" />
  </div>
</template>

<style lang="css" scoped>
.chart-dataset {
  height: 400px;
}
</style>
