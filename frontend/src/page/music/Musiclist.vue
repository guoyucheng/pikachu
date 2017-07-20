<template>
    <div class="music-musiclist">
        <heada :head='head' ></heada>
        
        <div class="wrap">
             <div class="music-banner">
                <mt-swipe :auto="3000">
                    <mt-swipe-item v-for="data in banner" key="data.id">
                        <img :src="data.src">
                    </mt-swipe-item>
                </mt-swipe>
            </div>
           <div class="typewrap">
                <div class="type-title">平台名称：{{ head.title }}</div>
                <ul class="typelist-ul3">
                    <li v-for="data in live_list" key="data.id">
                        <a href="JavaScript:" @click="play(data.id)">
                            <img class="typelist-img" :src="data.header_img" onerror="this.src='http://osrj8qkqk.bkt.clouddn.com/%E9%BB%98%E8%AE%A4%E5%9B%BE%E7%89%87.jpg'">
                            <p class="typelist-title">{{ data.name }}:{{ data.count }}</p>
                        </a>
                    </li>
                </ul>
            </div>

        </div>
        
    
    </div>
</template>

<script>
import heada from  "@/components/Head.vue"
import { getLiveList, getLive } from '../../api/api';
export default {
    name: 'music-musiclist',
    components: {
        heada,
    },
    data () {
        return {
            head:{
            },
            live_list: [],
            banner: [
                {'id':1, 'src':'http://p4.music.126.net/kXn-DuZHpWUt92wtn-kdJg==/18922595114158461.jpg'},
                {'id':2, 'src':'http://p3.music.126.net/OrppkkA9uzaq7w4m4M0hyQ==/18734578627590227.jpg'},
                {'id':3, 'src':'http://p3.music.126.net/ByeFpfshMXvOjnaiy886ug==/18888510253690479.jpg'},
                {'id':4, 'src':'http://p4.music.126.net/Fnw_tQevNEQFpN0V_Sx_kw==/18917097556020132.jpg'},
  
            ],

        }
    },
    mounted(){
        console.log(this.$route.query)
        this.head.title =  this.$route.query.title
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
        play(id){
            console.log(">>>>>D>>>>>",id);
            getLive({id: id}).then(data=>{
                
                console.log(data)
            })
        },

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* 音乐榜 banner  */
.music-banner{
    height: 200px;
}
.music-banner img{
    width: 100%;
    height: 100%;
    float: left;
}


/* 音乐榜分类  */
.typewrap{
    border-bottom: 1px solid #ccc;
}
.type-title{
    font-size: 1.2rem;
    line-height: 1.6rem;
    margin: 0.6rem 0;
    padding: 0 0.6rem;
    border-left: 5px solid red;
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
.typelist-img{
    width: 100%;
}
.typelist-title{
    height: 1.5rem;
    line-height: 1.5rem;
    overflow: hidden;
    font-size: 1rem;
    padding: 0 0.4rem
}
.typelist-updatetime{
    position: absolute;
    left: 0.6rem;
    top: 0.3rem;
    color: #666;
    font-size: 0.8rem;
}

</style>
