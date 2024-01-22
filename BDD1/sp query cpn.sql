USE [CPNVirtual]
GO
/****** Object:  StoredProcedure [dbo].[sp_cartera_credito_virtual]    Script Date: 07/18/2022 16:23:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Kevin,Quiroga>
-- Create date: <04/05/2022>
-- Description:	<Stored Procedure que permite realizar la consulta de un crédito virtual>
-- =============================================
ALTER PROCEDURE [dbo].[sp_cartera_credito_virtual]
	@i_tipo			CHAR(2),
	@t_trn		smallint 		= NULL,
	@i_desembolso		   char(1)	= NULL,
	@i_operacion	char(1)		= NULL,
	@i_modo	int	= NULL,
	@i_tipo_sol char(1)=NULL,
	@i_cliente		int	= NULL,
	@i_tipo_credito varchar(10)     = NULL,
	@i_tipo_plazo varchar(10)     = NULL,
	
	@r_banco           varchar(32)     = null,
	@s_servicio        tinyint         = null,
	@i_cedula          varchar(10)     = null,
	@s_cliente         int             = null,
	@i_novacion        char(1)         = 'N',
	@s_srv             varchar(30)  = null,
	@s_user            varchar(30)  = null,
	@s_term            varchar(10)  = null,
	@s_date            datetime  = null,
	@s_org             char(1)  = null,
	@s_ssn_branch      int			   = null,
	@s_perfil          smallint        = null,
	@i_destino         varchar(255)    = null,
	@r_val_cancelado   money           = 0,   
	@r_val_desembolsa  money           = 0,
	@i_monto           money           = 0,
	@i_plazo           smallint        = null,	
	@i_cod_oficina     int             = null,
	@i_reciprocidad    varchar(2)      = null, --ASA 2020.07.1 Código de reciprocidad (0:aportes, 1:encaje)
	@i_tipo_amor       varchar(30)     = null,
	@i_id_inst         int             = null, --INSTANCIA DEL PROCESO FLUJO CRE VIRTUAL
	@i_flujo           varchar(30)     = null, -- setCodigoCredito  CSA 2019.12,3 Flujo de credito (web / oficina)
	@i_tramite         int             = null,

	@i_origen          VARCHAR(10) = 'BVI',
	@i_tipotramite     char(1)     = 'O',
	@i_op_renovar      INT		   = NULL,
	@i_id_proceso      smallint    = 0,
	@i_toperacion      varchar(12) = null,
	@i_sector          varchar(10) = null,
	@i_moneda          tinyint     = 0,
	@i_fecha_ini       datetime    = null,
	@i_aportes         char(1)     = null,
	@i_servicio          int         = null
	

AS
BEGIN
	SET NOCOUNT ON;

	declare @sqla varchar(max)

	    if @i_tipo = 'GA' --Get informacion de la aplicacion de credito
		begin
				BEGIN TRY
				
					select @sqla = 'EXEC cob_bvirtual..sp_tr21_ingresa_solcre_cpn_bv @t_trn=@w_trn, @i_operacion="@w_operacion",@i_desembolso="@w_desembolso",@i_cliente=@w_cliente,@i_modo=@w_modo,@i_tipo_sol="@w_tipo_sol"'
					
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_desembolso',@i_desembolso)
					select @sqla = REPLACE(@sqla,'@w_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_modo',@i_modo)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
			


					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
								
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END
		
		if @i_tipo = 'GC' --getloancustomapplication
		begin
				BEGIN TRY
				
					select @sqla = 'EXEC cob_bvirtual..sp_tr21_ingresa_solcre_cpn_bv @t_trn=@w_trn, @i_operacion="@w_operacion",@i_cliente=@w_cliente,@i_tipo_sol="@w_tipo_sol"'
					
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_cliente',@i_cliente)


					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
								
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 
		
		if @i_tipo = 'GP' --getLoanPrequalifInfo
		begin
				BEGIN TRY
				
					select @sqla = 'EXEC cob_bvirtual..sp_tr21_ingresa_solcre_cpn_bv @t_trn=@w_trn, @i_operacion="@w_operacion",@i_cliente=@w_cliente,@i_tipo_sol="@w_tipo_sol",@i_tipo_credito="@w_tipo_credito"'
					
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_tipo_credito',@i_tipo_credito)


					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
								
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 
		
		if @i_tipo = 'VP' --Validacion de Plazos
		begin
				BEGIN TRY
				
					select @sqla = 'EXEC cob_bvirtual..sp_tr21_ingresa_solcre_cpn_bv @t_trn=@w_trn, @i_operacion="@w_operacion",@i_cliente=@w_cliente,@i_tipo_sol="@w_tipo_sol",@i_tipo_plazo="@w_tipo_plazo"'
					
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_tipo_plazo',@i_tipo_plazo)


					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
								
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 
		
		if @i_tipo = 'VM' --Validacion de Plazos
		begin
				BEGIN TRY
				
					select @sqla = 'EXEC cob_bvirtual..sp_tr21_ingresa_solcre_cpn_bv @t_trn=@w_trn, @i_operacion="@w_operacion",@i_cliente=@w_cliente,@i_tipo_sol="@w_tipo_sol",@i_tipo_credito="@W_tipo_credito"'
					
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_tipo_credito',@i_tipo_credito)


					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
								
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 


		if @i_tipo = 'VL' --GET CREDIT VIRTUAL LOCAL
		begin
			BEGIN TRY
			    select @sqla = 'EXEC cob_bvirtual..sp_tr_solcre_cpn_cw_bv
				@i_desembolso = "@w_desembolso", 
				@i_tipo_credito = "@w_tipo_credito",
				@t_trn =  @w_trn,
				@r_banco = "@w_banco",
				@i_tipo_sol = "@w_tipo_sol",
				@s_servicio =  @w_servicio, 
				@i_cedula = "@w_cedula", 
				@s_cliente =  @w_cliente, 
				@i_novacion = "@w_novacion", 
				@s_srv = "@w_srv", 
				@s_user = "@w_user", 
				@s_term = "@w_term", 
				@i_operacion = "@w_operacion", 
				@s_date =  "@w_date", 
				@s_org = "@w_org", 
				@s_ssn_branch = @w_ssn_branch, 
				@s_perfil = @w_perfil, 
				@i_destino = "@w_destino", 
				@r_val_cancelado = @w_val_cancelado,
				@r_val_desembolsa = @w_val_desembolsa,
				@i_monto = @w_monto,
				@i_plazo = @w_plazo,
				@i_cod_oficina = @w_cod_oficina,
				@i_tipo_amor = "@w_tipo_amor",
				@i_flujo = "@w_flujo",
				@i_tramite = @w_tramite
				'
				--print @sqla
					select @sqla = REPLACE(@sqla,'@w_desembolso',@i_desembolso)
					select @sqla = REPLACE(@sqla,'@w_tipo_credito',@i_tipo_credito)
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					select @sqla = REPLACE(@sqla,'@w_banco',@r_banco)
					select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_servicio',@s_servicio)
					select @sqla = REPLACE(@sqla,'@w_cedula',@i_cedula)
					select @sqla = REPLACE(@sqla,'@w_cliente',@s_cliente)
					select @sqla = REPLACE(@sqla,'@w_novacion',@i_novacion)
					select @sqla = REPLACE(@sqla,'@w_srv',@s_srv)
					select @sqla = REPLACE(@sqla,'@w_user',@s_user)
					select @sqla = REPLACE(@sqla,'@w_term',@s_term)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_date',@s_date)
					select @sqla = REPLACE(@sqla,'@w_org',@s_org)
					select @sqla = REPLACE(@sqla,'@w_ssn_branch',@s_ssn_branch)
					select @sqla = REPLACE(@sqla,'@w_perfil',@s_perfil)
					select @sqla = REPLACE(@sqla,'@w_destino',@i_destino)
					select @sqla = REPLACE(@sqla,'@w_val_cancelado',@r_val_cancelado)
					select @sqla = REPLACE(@sqla,'@w_val_desembolsa',@r_val_desembolsa)
					select @sqla = REPLACE(@sqla,'@w_monto',@i_monto)
					select @sqla = REPLACE(@sqla,'@w_plazo',@i_plazo)
					select @sqla = REPLACE(@sqla,'@w_cod_oficina',@i_cod_oficina)
					select @sqla = REPLACE(@sqla,'@w_tipo_amor',@i_tipo_amor)
					select @sqla = REPLACE(@sqla,'@w_flujo',@i_flujo)
					select @sqla = REPLACE(@sqla,'@w_tramite',@i_tramite)

					--print @sqla

					EXEC (@sqla) at LK_SQL_PQRS_CANALES

					if @@ROWCOUNT > 0
						begin
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 

		
		if @i_tipo = 'VC' --GET CREDIT VIRTUAL CENTER
		begin
			BEGIN TRY
				print 'entro vc'
			    select @sqla = 'EXEC cob_bvirtual..sp_tr21_procesa_solcre_cpn_bv
									@i_desembolso   = "@w_desembolso", 
									@i_tipo_credito = "@w_tipo_credito", 
									@t_trn =  @w_trn, 
									@s_servicio =  @w_servicio, 
									@i_cedula = "@w_cedula", 
									@i_cliente =  @wi_cliente,
									@i_novacion = "@w_novacion", 
									@s_srv = "@w_srv", 
									@s_user = "@w_user", 
									@s_term = "@w_term", 
									@i_operacion = "@w_operacion", 
									@s_date =  "@w_date", 
									@s_org = "@w_org", 
									@s_ssn_branch = @w_ssn_branch, 
									@s_perfil = @w_perfil, 
									@i_destino = "@w_destino", 
									@i_monto = @w_monto,
									@i_reciprocidad = "@w_reciprocidad",
									@i_tipo_amor = "@w_tipo_amor",
									@i_id_inst = @w_id_inst,
									@i_flujo = "@w_flujo",
									@i_tramite = @w_tramite
									'
									
					
					select @sqla = REPLACE(@sqla,'@w_desembolso',@i_desembolso)
					select @sqla = REPLACE(@sqla,'@w_tipo_credito',@i_tipo_credito)
					select @sqla = REPLACE(@sqla,'@w_trn',@t_trn)
					--select @sqla = REPLACE(@sqla,'@w_banco',@r_banco)
					--select @sqla = REPLACE(@sqla,'@w_tipo_sol',@i_tipo_sol)
					select @sqla = REPLACE(@sqla,'@w_servicio',@s_servicio)
					select @sqla = REPLACE(@sqla,'@w_cedula',@i_cedula)
					select @sqla = REPLACE(@sqla,'@wi_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_novacion',@i_novacion)
					select @sqla = REPLACE(@sqla,'@w_srv',@s_srv)
					select @sqla = REPLACE(@sqla,'@w_user',@s_user)
					select @sqla = REPLACE(@sqla,'@w_term',@s_term)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_date',@s_date)
					select @sqla = REPLACE(@sqla,'@w_org',@s_org)
					select @sqla = REPLACE(@sqla,'@w_ssn_branch',@s_ssn_branch)
					select @sqla = REPLACE(@sqla,'@w_perfil',@s_perfil)
					select @sqla = REPLACE(@sqla,'@w_destino',@i_destino)
					
					--select @sqla = REPLACE(@sqla,'@w_val_cancelado',@r_val_cancelado)
					--select @sqla = REPLACE(@sqla,'@w_val_desembolsa',@r_val_desembolsa)
					select @sqla = REPLACE(@sqla,'@w_monto',@i_monto)
					
					select @sqla = REPLACE(@sqla,'@w_reciprocidad',@i_reciprocidad)
					
					select @sqla = REPLACE(@sqla,'@w_tipo_amor',@i_tipo_amor)
					
					select @sqla = REPLACE(@sqla,'@w_id_inst',@i_id_inst)
					select @sqla = REPLACE(@sqla,'@w_flujo',@i_flujo)
					select @sqla = REPLACE(@sqla,'@w_tramite',@i_tramite)
					
					print @sqla				

					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 
		
		if @i_tipo = 'VR' --GET ValidationRequest
		begin
			BEGIN TRY
			    select @sqla = 'EXEC cob_workflow..sp_evalua_crevirtual
									@i_operacion  = "@w_operacion", 
									@i_origen	  = "@w_origen",
									@i_toperacion = "@w_toperacion",
									@i_cliente =  @wi_cliente,
									@i_tipotramite = @w_tipotramite,
									@i_op_renovar = @w_op_renovar,
									@i_id_proceso = @w_id_proceso,
									@i_monto = @w_monto,
									@i_plazo = @w_plazo,
									@s_srv = "@w_srv", 
									@s_user = "@w_user", 
									@s_term = "@w_term", 
									@s_date =  "@w_date", 
									@s_org = "@w_org"
									'
									/**/
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_origen',@i_origen)
					select @sqla = REPLACE(@sqla,'@w_toperacion',@i_toperacion)
					select @sqla = REPLACE(@sqla,'@wi_cliente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_tipotramite',@i_tipotramite)
					select @sqla = REPLACE(@sqla,'@w_op_renovar',@i_op_renovar)
					select @sqla = REPLACE(@sqla,'@w_id_proceso',@i_id_proceso)
					select @sqla = REPLACE(@sqla,'@w_monto',@i_monto)
					select @sqla = REPLACE(@sqla,'@w_plazo',@i_plazo)
					select @sqla = REPLACE(@sqla,'@w_srv',@s_srv)
					select @sqla = REPLACE(@sqla,'@w_user',@s_user)
					select @sqla = REPLACE(@sqla,'@w_term',@s_term)
					select @sqla = REPLACE(@sqla,'@w_date',@s_date)
					select @sqla = REPLACE(@sqla,'@w_org',@s_org)

					print @sqla

					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		END 

		if @i_tipo = 'SP' --GET sp_bv_simulador_prestamos
		begin
			BEGIN TRY
				print 'entro SP sp_bv_simulador_prestamos'

			    select @sqla = 'EXEC cobis..sp_bv_simulador_prestamos
										@i_sector = "@w_sector",
										@i_tipo_amortizacion = "@w_tipo_amortizacion",
										@i_fecha_ini = "@w_fecha_ini",
										@i_moneda = @w_moneda,
										@i_monto = @w_monto,
										@i_plazo = @w_plazo,
										@i_operacion  = "@w_operacion",
										@i_toperacion = "@w_toperacion",
										@i_aportes = "@w_aportes",
										@s_user = "@w_user",
										@s_term = "@w_term", 
										@s_date =  "@w_date"'

					---print @sqla

					select @sqla = REPLACE(@sqla,'@w_sector',@i_sector)
					select @sqla = REPLACE(@sqla,'@w_tipo_amortizacion',@i_tipo_amor)
					select @sqla = REPLACE(@sqla,'@w_fecha_ini', @i_fecha_ini)
					select @sqla = REPLACE(@sqla,'@w_moneda',@i_moneda)
					select @sqla = REPLACE(@sqla,'@w_monto',@i_monto)
					select @sqla = REPLACE(@sqla,'@w_plazo',@i_plazo)
					select @sqla = REPLACE(@sqla,'@w_operacion',@i_operacion)
					select @sqla = REPLACE(@sqla,'@w_toperacion',@i_toperacion)
					select @sqla = REPLACE(@sqla,'@w_aportes',@i_aportes)
					select @sqla = REPLACE(@sqla,'@w_user',@s_user)
					select @sqla = REPLACE(@sqla,'@w_term',@s_term)
					select @sqla = REPLACE(@sqla,'@w_date',@s_date)
					
					--print @sqla

					EXEC (@sqla) at LK_SYB_PQRS_N1

					if @@ROWCOUNT > 0
						begin
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		end

		if @i_tipo = 'CP' --GET sp_cons_cap_pago_aprob
		begin
			BEGIN TRY
				print 'entro SP cob_credito..sp_cons_cap_pago_aprob'

			    select @sqla = 'EXEC cob_credito..sp_cons_cap_pago_aprob
										@i_ente = @w_ente,
										@i_servicio = @w_servicio,
										@i_tipo_credito = "@w_tipo_credito"
										'
					---print @sqla
					select @sqla = REPLACE(@sqla,'@w_ente',@i_cliente)
					select @sqla = REPLACE(@sqla,'@w_servicio', @i_servicio)
					select @sqla = REPLACE(@sqla,'@w_tipo_credito',@i_tipo_credito)
				
				print @sqla
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    					EXEC (@sqla) at LK_SYB_PQRS

					if @@ROWCOUNT > 0
						begin
							exec cpn_error @i_codigo = 0
						end
					else
						begin
							exec cpn_error @i_codigo = 10002
						end

				END TRY
				BEGIN CATCH
				  SELECT
					ERROR_NUMBER() AS ErrorNumber,
					ERROR_STATE() AS ErrorState,
					ERROR_SEVERITY() AS ErrorSeverity,
					ERROR_PROCEDURE() AS ErrorProcedure,
					ERROR_LINE() AS ErrorLine,
					ERROR_MESSAGE() AS ErrorMessage;

					exec cpn_error @i_codigo = 10002
				END CATCH;
		end




END