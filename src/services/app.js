import api from "@/plugins/api";

class AppService {
    async getCharts() {
        console.log("get charts");
        try {
            const { data } = await api.get('/charts');
            console.log("RESULTADO DA BUSCA", data.results);
            return data.results;
        } catch (error) {
            console.log("error in get charts", error);
            // throw error;
        }
    }
}

export default new AppService();