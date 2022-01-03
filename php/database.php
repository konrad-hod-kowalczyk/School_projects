<?php
    class P
    {
        public $host;
        public $db_user;
        public $db_password;
        public $db_name;
        function __construct($host,$db_user,$db_password,$db_name)
        {
            $this->host = $host;
            $this->db_user = $db_user;
            $this->db_password = $db_password;
            $this->db_name = $db_name;
        }
    }
    $data = new P('localhost','root','','logowanie');
?>