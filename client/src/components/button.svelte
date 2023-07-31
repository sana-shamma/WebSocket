<script>
    export let value = "" ;
    export let id = "" ;
    export let onClick = ()=>{}
</script>

<button on:click={() => onClick()} id={id}>{value}</button>

<style>
    button{
        border-radius: 30px;
        width: 90px;
        height: 30px;
        color: white;
        border: none;
        cursor: pointer;
    }
    #delete{
        background-color: red;
    }
    #add{
        background-color: rgb(0, 218, 146);
        width: 150px;
        height: 50px;
    }
    #display{
        background-color: coral;
        width: 150px;
        height: 50px;
    }
</style>