const base = {
    get() {
        return {
            url : "http://localhost:8080/django4bp03j2o/",
            name: "django4bp03j2o",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "动漫推荐系统"
        } 
    }
}
export default base
