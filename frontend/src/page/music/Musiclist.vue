<template>
    <div class="music-musiclist">
        <heada :head='head' ></heada>
        
        <div class="wrap">
            <div class="list_panel_bd clearfix">
                
                       <!--  <ul class="typelist-ul3">
                            <li v-for="data in live_list" key="data.id">
                                <router-link :to='{name:"musiclist", query:{ id:data.id, title:data.name } }'>
                                    <img class="typelist-img" :src="data.header_img" onerror="this.src='http://p4.music.126.net/N2whh2Prf0l8QHmCpShrcQ==/19140298416347251.jpg?param=150y150'">
                                    <p class="typelist-title">{{ data.name }}:{{ data.count }}</p>
                                </router-link>
                            </li>
                        </ul> -->

                <div v-for="data in live_list" key="data.id" class="list_box">
                         <div class="list_pic">
                                 <img class="typelist-img" :src="data.header_img" onerror="this.src='http://p4.music.126.net/N2whh2Prf0l8QHmCpShrcQ==/19140298416347251.jpg?param=150y150'">
                         </div>
                         <div class="list_user_info">
                                <span class="list_user_head" style="background-image: url(data.header_img)"></span>
                                <span class="list_user_name">{{ data.name }}</span>
                            </div>
                </div>
                
            </div>

        </div>
        
    
    </div>
</template>

<script>
import heada from  "@/components/Head.vue"
import { getLiveList } from '../../api/api';
export default {
    name: 'music-musiclist',
    components: {
        heada,
    },
    data () {
        return {
            head:{
                title:'音乐榜'
            },
            live_list: [],

        }
    },
    mounted(){
        console.log(this.$route.query)
        this.head= {
            title : this.$route.query.title
        }
        console.log(this.head)
        this.LiveList();        
    },
    methods:{
        LiveList(){
            getLiveList({id:this.$route.query.id}).then(data=>{
                this.live_list = data.data.items;
                console.log(this.live_list)
            })
        },

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.clearfix:before, .clearfix:after {
    content: " ";
    display: table;
}
.clearfix:after {
    clear: both;
}
.clearfix:before, .clearfix:after {
    content: " ";
    display: table;
}
.list_box {
    float: left;
    margin-right: 11px;
    margin-bottom: 10px;
    width: 150px;
    background-color: #fff;
    box-shadow: 0 0 3px #ddd;
}
.list_pic {
    overflow: hidden;
    position: relative;
}
.list_user_info {
    padding: 15px 0 5px;
}
user agent stylesheet
div {
    display: block;
}
live.css:1
.list_pic, .list_pic a {
    color: #fff;
    cursor: pointer;
}
.typelist-ul2, .typelist-ul3{
    width: 96%;
    height: auto;
    margin: auto;
    overflow: hidden;
}
.typelist-ul2 li, .typelist-ul3 li{
    position: relative;
    float: left;
    height: auto;
    margin: 0.2rem 2% 0.8rem 2%;
}
.typelist-ul2 li{
    width: 46%;
}
.typelist-ul3 li{
    width: 29%;  
}

</style>
