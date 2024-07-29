import { defineStore } from "pinia";
import { computed, reactive } from "vue";
import AppService from "@/services/app";

export const useAppStore = defineStore("app",
    () => {
      const state = reactive({
        loading: false,
        error: null,
        theme: "light",
        datas: {
          mainChart: {
            lines: [
                {
                  data: [],
                },
                {
                  data: [],
                },
            ],
            pie: {
                data: [
                  { value: 0, name: "" },
                  { value: 0, name: "" },
                ],
                label: {
                  color: '#000',
                },
            },
            dataframe: null,
        },
          globalIndicators: {
            committed: 0,
            settled: 0,
            balance: 0
          },
        }
      });

      const isDark = computed(() => state.theme === 'dark');
      const themeColor = computed(() => state.theme);
      const isLoading = computed(() => state.loading);
      const committed = computed(() => state.datas.globalIndicators.committed);
      const settled = computed(() => state.datas.globalIndicators.settled);
      const balance = computed(() => state.datas.globalIndicators.balance);
      const mainDataframe = computed(() => state.datas.mainChart.dataframe);
      const mainChart = computed(() => {
        return {
          title: { text: "" },
          tooltip: { trigger: "axis" },
          legend: { 
            data: ["Liquidado", "Empenhado"], 
            left: "1%",
          },
          grid: { left: "1%", right: "23.5%", bottom: "3%", containLabel: true },
          toolbox: { feature: { saveAsImage: {} } },
          xAxis: {
            type: "category",
            boundaryGap: false,
            axisLabel: { margin: 20 },
          },
          yAxis: { type: "value" },
          series: [
            {
              name: "Liquidado",
              type: "line",
              stack: "Liquidado",
              smooth: true,
              data: state.datas?.mainChart?.lines?.[0]?.data || [],
            },
            {
              name: "Empenhado",
              type: "line",
              stack: "Empenhado",
              smooth: true,
              data: state.datas?.mainChart?.lines?.[1]?.data || [],
            },
            {
              name: "Soma Total (R$)",
              type: "pie",
              radius: "60%",
              center: ["90%", "50%"],
              emphasis: {
                label: {
                  show: true,
                },
              },
              label: {
                show: false,
                formatter: "{d}%",
                fontSize: 15,
                fontWeight: "bold",
                position: "center",
                color: state.theme == 'dark' ? "#fff" : "#000",
              },
              data: state.datas?.mainChart?.pie?.data || [],
            },
          ],
        };
      });

      const setTheme = (theme) => {
        state.theme = theme;
      }

      const getCharts = async () => {
          state.loading = true;
          try {
            state.datas = await AppService.getCharts();
          } catch (error) {
            state.error = error;
          } finally {
            state.loading = false;
          }
      }

      return {
          state,
          themeColor,
          isDark,
          isLoading,
          committed,
          settled,
          balance,
          mainChart,
          mainDataframe,
          setTheme,
          getCharts,
      };
    }
)
