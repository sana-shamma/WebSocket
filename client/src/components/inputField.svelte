<script>
    export let title;
    export let id;
    export let value;
</script>
<label for={id}>{title}</label>
<input bind:value={value} id={id} type="text"/>