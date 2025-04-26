<script>
import BodyComp from'@/components/layout/Body.vue'
import HederComp from'@/components/layout/Heder.vue'
import NavComp from'@/components/layout/Nav.vue'
import { useRouter ,useRoute} from 'vue-router'
import{ref}from'vue'
export default{
    name:'HomeComp',
    components:{
        BodyComp,
        NavComp,
        HederComp
    },
    
    setup(){
        const route=useRoute()
        const router=useRouter()
        //console.log(route.query.name)
        const userData = ref(route.query)
        const name1=ref(route.query.username)
        function loginout(){
            router.push('/login')
            localStorage.removeItem('token')
        }

        return {
            loginout,
            name1,
            userData
        }
    }
}

</script>
<template>
    <!-- <heder-comp :username="name1" :loginout="loginout"></heder-comp> -->
    <div class="body1">
        <!-- <nav-comp :userData="userData" :username="name1"></nav-comp> -->
    <body-comp></body-comp>


    </div>
    
</template>
<style scoped>
.body1{
    height:calc(100%);
    width: 100%;
    display: flex;
}
</style>