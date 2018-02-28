$(document).ready(function(){
    $('#schedule').DataTable({
       "lengthChange": false,
       "searching": false
    });

    $('#position').DataTable({
       "lengthChange": false,
       "searching": false,
       "responsive": true
    });

    $('#movement').DataTable({
       "lengthChange": false,
       "searching": false,
       "responsive": true
    });
});
