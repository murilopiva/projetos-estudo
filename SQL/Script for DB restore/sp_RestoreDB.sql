-- MURILO PIVA - 04/06/2020


--para ativar o xp_cmdshell caso o servidor não esteja configurado.
sp_configure 'advanced options', 1
RECONFIGURE
go
sp_configure 'xp_cmdshell', 1
RECONFIGURE
go


use master
go

if exists (select routine_name from INFORMATION_SCHEMA.routines where routine_name = 'sp_RestoreDB')
	drop procedure sp_RestoreDB
go

create procedure sp_RestoreDB (@caminhoBAK as varchar(1000), @caminhoMDFLDF Nvarchar(max), @nomeBD nvarchar(50), @fl_excluirBAK as char(1) = 'N')
as
	set nocount on

	DECLARE @LogicalNameData VARCHAR(128), @LogicalNameLog VARCHAR(128)

	if exists (select name from sys.databases where name = @nomeBD)
	begin
		raiserror ('Banco já restaurado!',16,1)
		return
	end 

	if len(@caminhobak) = 0
	begin
		raiserror ('Caminho para buscar o arquivo .BAK não informado!',16,1)
		return
	end 

	if len(@caminhoMDFLDF) = 0
	begin
		raiserror ('Caminho para salvar os arquivos .MDF e .LDF não informado!',16,1)
		return
	end 

	DECLARE @Table TABLE
		(
		  LogicalName VARCHAR(128) ,
		  [PhysicalName] VARCHAR(128) ,
		  [Type] VARCHAR ,
		  [FileGroupName] VARCHAR(128) ,
		  [Size] VARCHAR(128) ,
		  [MaxSize] VARCHAR(128) ,
		  [FileId] VARCHAR(128) ,
		  [CreateLSN] VARCHAR(128) ,
		  [DropLSN] VARCHAR(128) ,
		  [UniqueId] VARCHAR(128) ,
		  [ReadOnlyLSN] VARCHAR(128) ,
		  [ReadWriteLSN] VARCHAR(128) ,
		  [BackupSizeInBytes] VARCHAR(128) ,
		  [SourceBlockSize] VARCHAR(128) ,
		  [FileGroupId] VARCHAR(128) ,
		  [LogGroupGUID] VARCHAR(128) ,
		  [DifferentialBaseLSN] VARCHAR(128) ,
		  [DifferentialBaseGUID] VARCHAR(128) ,
		  [IsReadOnly] VARCHAR(128) ,
		  [IsPresent] VARCHAR(128) ,
		  [TDEThumbprint] VARCHAR(128)
		)

	--buscar o nome logico do arquivo bkp.
	INSERT INTO @table
		EXEC ('RESTORE FILELISTONLY FROM DISK=''' + @caminhoBAK + '''')

	-- cria a query base para restore
	DECLARE @restoreScript NVARCHAR(max)='RESTORE DATABASE ' + @nomeBD + ' FROM DISK =''' + @caminhoBAK + ''' WITH FILE = 1 '

	--move os arquivos .mdf e .ldf para o local desejado
	SELECT  @restoreScript +=CHAR(10) + ' ,MOVE  ''' +  LogicalName + ''' TO ''' + 
			@caminhoMDFLDF  + LogicalName + RIGHT(PhysicalName,4) + ''''
	FROM   @Table
	WHERE  Type = 'D'

	--move os arquivos .mdf e .ldf para o local desejado
	SELECT  @restoreScript += ' ,MOVE  ''' +  LogicalName + ''' TO ''' + @caminhoMDFLDF  + LogicalName + '.ldf'''
	FROM    @Table
	WHERE   Type = 'L'

	--stats 10 para mostrar percentual do restore
	SET @restoreScript += ' , NOUNLOAD, REPLACE, STATS = 10 '
	
	exec sp_executesql @restoreScript

	if @fl_excluirBAK = 'S'
		exec xp_cmdshell caminhoBAK

	set nocount off
go

--sp_RestoreDB N'D:\Bancos\SQL2008\teste.bak', 'D:\Bancos\SQL2008\', N'BD_RESTORED'

